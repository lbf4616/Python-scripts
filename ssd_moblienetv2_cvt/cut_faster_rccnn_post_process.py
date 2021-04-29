# coding: UTF-8
import json
import os
from collections import defaultdict

import tensorflow as tf
import tensorflow.compat.v1 as tf_compat_v1
from absl import flags
from google.protobuf import text_format
from tensorflow.python.platform import gfile

# Running input parameters definition.
FLAGS = flags.FLAGS
flags.DEFINE_string(
    name="model_file",
    default="/disk/huansheng_inspection_pipeline/solar_defect_detection_vi/models_nvidia/vi_ssd_single_0316.pb",
    # /frozen_inference_graph.pb",
    help="Path to frozen infer graph pb file ",
)
flags.DEFINE_string("output_dir", ".", "Path to cut pb file to be written.")
flags.DEFINE_boolean("convert_to_pbtxt", True,
                     "Whether convert the cut pb file to pbtxt file.")
flags.DEFINE_boolean(
    "delete_tmp_file", False, "Whether deleted intermediate file including "
    "names_of_deleted_nodes.txt,  names_of_nodes_input_del.txt, identity.pb")
flags.mark_flag_as_required('model_file')

IDENTITY_PB_FILE = "identity.pb"
DEFAULT_FILE_NAME_FOR_WRITE_DEL_NAMES = "names_of_deleted_nodes.txt"
DEFAULT_FILE_NAME_FOR_INPUT_DEL_NAMES = "names_of_nodes_input_del.txt"
IDENTITY_PBTXT = """node {
  name: "num_boxes"
  op: "Identity"
  input: "IDENTITY_INPUT_NAME"
  attr {
    key: "T"
    value {
      type: DT_INT32
    }
  }
}"""

HANG_NODES = [
    "detection_boxes",
    "detection_scores",
    "detection_multiclass_scores",
    "add/y",
    "add",
    "detection_classes",
    "num_detections",
    "Postprocessor/Cast_1",
    "Postprocessor/Cast_2",
    "Postprocessor/Cast_2/x",
    "Postprocessor/Cast_3/x",
    "Postprocessor/Cast_3",
    "Postprocessor/Cast_4",
    "Postprocessor/truediv_1",
    "Postprocessor/unstack",
    "Postprocessor/truediv",
    "Postprocessor/zeros_like_1",
    "Postprocessor/zeros_like",
    "Postprocessor/stack_1",
]


def find_nodes_with_prefix_and_postfix(
    input_pb,
    prefix="BatchMultiClassNonMaxSuppression/map/TensorArrayStack_",
    postfix="TensorArrayGatherV3",
):
    with open(input_pb, "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

    graph_nodes = graph_def.node
    graph_node_names = [node.name for node in graph_nodes]
    node_names = [
        name for name in graph_node_names
        if name.startswith(prefix) and name.endswith(postfix)
    ]
    print(f"found node name:{node_names[0]}, "
          f"starts with:{prefix}, endswith:{postfix}")
    return node_names[0]


def convert_pbtxt_to_pb(filename, converted_pb_name):
    with gfile.FastGFile(filename, "r") as f:
        graph_def = tf.compat.v1.GraphDef()
        text_format.Merge(f.read(), graph_def)
        tf.compat.v1.train.write_graph(
            graph_def,
            os.path.dirname(converted_pb_name),
            os.path.basename(converted_pb_name),
            as_text=False,
        )

def convert_pbtxt_content_to_pb(pbtxt_content, converted_pb_name):
    graph_def = tf.compat.v1.GraphDef()
    text_format.Merge(pbtxt_content, graph_def)
    tf.compat.v1.train.write_graph(
        graph_def,
        os.path.dirname(converted_pb_name),
        os.path.basename(converted_pb_name),
        as_text=False,
    )


def get_identity_graph_nodes(input_pb):
    identity_node_input = find_nodes_with_prefix_and_postfix(input_pb)
    identity_pb_content = IDENTITY_PBTXT.replace("IDENTITY_INPUT_NAME",
                                                 identity_node_input)
    output_dir = FLAGS.output_dir
    identity_tmp_pb = os.path.join(output_dir, IDENTITY_PB_FILE)
    convert_pbtxt_content_to_pb(identity_pb_content, identity_tmp_pb)
    with open(identity_tmp_pb, "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

    if FLAGS.delete_tmp_file:
        output_dir = FLAGS.output_dir
        identity_tmp_pb = os.path.join(output_dir, IDENTITY_PB_FILE)
        os.remove(identity_tmp_pb)

    return graph_def.node


def del_nodes_name_with_kw(
    input_model_filepath,
    output_dir,
    nmskw="Postprocessor/BatchMultiClassNonMaxSuppression",
    prekw="Preprocessor/map",
    del_names_file=DEFAULT_FILE_NAME_FOR_WRITE_DEL_NAMES,
):
    with open(input_model_filepath, "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

    nodes_to_keep = []
    names_to_del = []
    for node in graph_def.node:
        if prekw in node.name or nmskw in node.name or node.name in HANG_NODES:
            names_to_del.append(node.name)
        else:
            nodes_to_keep.append(node)

    mod_graph_def = tf.GraphDef()
    mod_graph_def.node.extend(nodes_to_keep)

    print("Num of deleted nodes:", len(names_to_del))
    print("Deleted nodes names write to: names_of_deleted.txt")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if not FLAGS.delete_tmp_file:
        del_full_name = os.path.join(output_dir, del_names_file)
        with open(del_full_name, "a+") as f:
            f.write("\n".join(names_to_del))

    # Handle nodes' input that has been deleted
    deleted_input_names = defaultdict(list)
    for node in mod_graph_def.node:
        input_keep_names = []
        input_del_names = []
        for input_name in node.input:
            if input_name not in names_to_del:
                input_keep_names.append(input_name)
            else:
                input_del_names.append(input_name)

        del node.input[:]
        node.input.extend(input_keep_names)
        if input_del_names:
            deleted_input_names[node.name] = input_del_names[:]

        if node.name == 'Preprocessor/mul':
            del node.input[:]
            node.input.extend(['Preprocessor/mul/x', 'Cast'])

    # New constant to add================================
    # identity_node = get_identity_graph_nodes(input_model_filepath)
    # print("Identity node:", identity_node[0])
    # mod_graph_def.node.extend(identity_node)
    # New constant to add================================

    input_file_name = os.path.basename(input_model_filepath)
    final_pb_file = os.path.join(
        output_dir, "_cut".join(os.path.splitext(input_file_name)))
    with open(final_pb_file, "wb") as f:
        f.write(mod_graph_def.SerializeToString())

    print("num of node input has been removed:", len(deleted_input_names))
    if not deleted_input_names:
        return final_pb_file

    if not FLAGS.delete_tmp_file:
        output_dir = os.path.dirname(input_model_filepath)
        file_to_rcd_nodes_name_input_del = os.path.join(
            output_dir, DEFAULT_FILE_NAME_FOR_INPUT_DEL_NAMES)
        with open(file_to_rcd_nodes_name_input_del, "w") as fw:
            fw.write(json.dumps(deleted_input_names))

    return final_pb_file


def convert_pb_to_pbtxt(filename, tmp_pbtxt):
    with gfile.FastGFile(filename, "rb") as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name="")

        tf.compat.v1.train.write_graph(
            graph_def,
            os.path.dirname(tmp_pbtxt),
            os.path.basename(tmp_pbtxt),
            as_text=True,
        )


def cut_faster_rcnn_post_process_nodes(
    input_pb_file,
    output_dir,
    del_names_file=DEFAULT_FILE_NAME_FOR_WRITE_DEL_NAMES,
):
    final_pb_file = del_nodes_name_with_kw(input_pb_file,
                                           output_dir,
                                           del_names_file=del_names_file)

    if FLAGS.convert_to_pbtxt:
        convert_pb_to_pbtxt(final_pb_file, final_pb_file + "txt")


def main(unused_argv):  # Can not delete this arg
    #input_pb_file = FLAGS.model_file
    #output_dir = FLAGS.output_dir
    #cut_faster_rcnn_post_process_nodes(input_pb_file, output_dir)
    cut_faster_rcnn_post_process_nodes("/disk/huansheng_inspection_pipeline/solar_defect_detection_vi/models_nvidia/vi_ssd_single_0316.pb", "/disk/huansheng_inspection_pipeline/solar_defect_detection_vi/models_nvidia")


if __name__ == "__main__":
    tf_compat_v1.app.run()
