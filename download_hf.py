from __future__ import absolute_import, division, print_function

import sys
import os
import argparse
import time
import pdb
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--bert_model_name_or_path", type=str, default='bert-base-uncased',
                        help="Path to pre-trained model or shortcut name(ex, bert-base-uncased)")
    parser.add_argument("--bert_do_lower_case", action="store_true",
                        help="Set this flag if you are using an uncased model.")
    parser.add_argument("--bert_output_dir", type=str, default='bert-checkpoint',
                        help="The output directory where the model predictions and checkpoints will be written.")

    opt = parser.parse_args()

    from transformers import BertTokenizer, BertConfig, BertModel
    # download
    logger.info("[Downloading transformers...]")
    bert_tokenizer = BertTokenizer.from_pretrained(opt.bert_model_name_or_path,
                                                   do_lower_case=opt.bert_do_lower_case)
    bert_model = BertModel.from_pretrained(opt.bert_model_name_or_path,
                                           from_tf=bool(".ckpt" in opt.bert_model_name_or_path))
    bert_config = bert_model.config
    logger.info("[Done]")
    # save
    if not os.path.exists(opt.bert_output_dir):
        os.makedirs(opt.bert_output_dir)
    bert_tokenizer.save_pretrained(opt.bert_output_dir)
    bert_model.save_pretrained(opt.bert_output_dir)
    logger.info("[Saved to {}]".format(opt.bert_output_dir)
 
if __name__ == '__main__':
    main()