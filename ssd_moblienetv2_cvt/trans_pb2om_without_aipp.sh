export PATH=/usr/local/python3.7.5/bin:/usr/local/Ascend/ascend-toolkit/latest/atc/ccec_compiler/bin:/usr/local/Ascend/ascend-toolkit/latest/atc/bin:$PATH
export PYTHONPATH=/usr/local/Ascend/ascend-toolkit/latest/atc/python/site-packages:/usr/local/Ascend/ascend-toolkit/latest/atc/python/site-packages/auto_tune.egg/auto_tune:$/usr/local/Ascend/ascend-toolkit/latest/atc/python/site-packages/schedule_search.egg
export LD_LIBRARY_PATH=/usr/local/Ascend/ascend-toolkit/latest/atc/lib64:$LD_LIBRARY_PATH
export ASCEND_OPP_PATH=/usr/local/Ascend/ascend-toolkit/latest/opp
export SLOG_PRINT_TO_STDOUT=1

/usr/local/Ascend/ascend-toolkit/latest/atc/bin/atc --model=./ssd_cut.pb \
    --framework=3 \
    --output=./ssd.js \
    --input_shape="image_tensor:1,300,300,3" \
	--output_type=FP32 \
    --soc_version=Ascend310 \
	--log=info
