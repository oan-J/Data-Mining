#! /usr/bin/env bash
export NCCL_P2P_DISABLE="1"
export NCCL_IB_DISABLE="1"
set -ex

LR=1e-4
NUM_GPUS=4
MAX_SOURCE_LEN=1024
MAX_TARGET_LEN=128
DEV_BATCH_SIZE=1
GRAD_ACCUMULARION_STEPS=16
MAX_STEP=500
SAVE_INTERVAL=500

RUN_NAME=crazy_literature_with_scene_and_rate
BASE_MODEL_PATH=../chatglm3-6b
DATASET_PATH=data/文章内容-分割-去重_output_processed.jsonl

DATESTR=`date +%Y%m%d-%H%M%S`
OUTPUT_DIR=output/${RUN_NAME}-${DATESTR}-${LR}
MASTER_PORT=$(shuf -n 1 -i 10000-65535)

mkdir -p $OUTPUT_DIR

torchrun --standalone --nnodes=1 --nproc_per_node=$NUM_GPUS finetune.py \
    --train_format input-output \
    --train_file $DATASET_PATH \
    --preprocessing_num_workers 1 \
    --model_name_or_path $BASE_MODEL_PATH \
    --output_dir $OUTPUT_DIR \
    --max_source_length $MAX_SOURCE_LEN \
    --max_target_length $MAX_TARGET_LEN \
    --per_device_train_batch_size $DEV_BATCH_SIZE \
    --gradient_accumulation_steps $GRAD_ACCUMULARION_STEPS \
    --max_steps $MAX_STEP \
    --logging_steps 1 \
    --save_steps $SAVE_INTERVAL \
    --learning_rate $LR \
    --fp16 \
    --quantization_bit 8\
    --deepspeed configs/deepspeed.json 2>&1 | tee ${OUTPUT_DIR}/train.log
