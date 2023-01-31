import torch
import torch.nn as nn
import transformers

from transformers import (AutoTokenizer, AutoModelForSequenceClassification, 
                          PreTrainedModel, DistilBertModel, DistilBertForSequenceClassification)
from transformers.modeling_outputs import SequenceClassifierOutput


class DistilBertForMultilabelSequenceClassification(DistilBertForSequenceClassification):
    def __init__(self, config, linear_dropout_prob = 0.5):
      super().__init__(config)
      self.batch_norm = nn.BatchNorm1d(config.hidden_size)
      self.dropout = nn.Dropout(linear_dropout_prob)
      self.classifier = nn.Linear(config.hidden_size, self.config.num_labels)
      self.sigmoid = nn.Sigmoid()



      self.init_weights()

    def forward(self,
        input_ids=None,
        attention_mask=None,
        head_mask=None,
        inputs_embeds=None,
        labels=None,
        output_attentions=None,
        output_hidden_states=None,
        return_dict=None):
        return_dict = return_dict if return_dict is not None else self.config.use_return_dict

        outputs = self.distilbert(
            input_ids,
            attention_mask=attention_mask,
            head_mask=head_mask,
            inputs_embeds=inputs_embeds,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict)

        hidden_state = outputs[0]
        pooled_output = hidden_state[:, 0]
        pooled_output = self.batch_norm(pooled_output)
        pooled_output = self.dropout(pooled_output)
        logits = self.classifier(pooled_output)

        loss = None
        if labels is not None:
            loss_fct = torch.nn.BCEWithLogitsLoss()
            loss = loss_fct(logits.view(-1, self.num_labels),
                            labels.float().view(-1, self.num_labels))

        if not return_dict:
            output = (logits,) + outputs[2:]
            return ((loss,) + output) if loss is not None else output

        return SequenceClassifierOutput(loss=loss,
            logits=logits,
            hidden_states=outputs.hidden_states,
            attentions=outputs.attentions)
