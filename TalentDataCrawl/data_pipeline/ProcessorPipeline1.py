from processor.IrrelevantProcessor.ProcessorByKeyWord import ProcessorByKeyWord
from processor.DuplicateProcessor.ProcessorByTFIDF import ProcessorByTFIDF
from processor.LocationExtractProcessor.ProcessorBySpacyModel import ProcessorBySpacyModel
from processor.CategoryClassifyProcessor.ProcessorByBiRnn import ProcessorByBiRnn
from processor.TalentInfoProcessor.ProcessorByKeyAndPattern import ProcessorByKeyAndPattern


class ProcessorPipeline1:
    def __init__(self):
        self.name = "data pipeline 1"
        self.elastic_search_index = "talent-cleaned-e1"
        processor_irrelevant_keyword = ProcessorByKeyWord()
        processor_duplicate_tf_idf = ProcessorByTFIDF("talent-cleaned-e1")
        processor_ner_spacy_model = ProcessorBySpacyModel()
        processor_cate_classify = ProcessorByBiRnn()
        processor_talent_info = ProcessorByKeyAndPattern()

        self.processors = [
            processor_irrelevant_keyword,
            processor_duplicate_tf_idf,
            processor_ner_spacy_model,
            processor_cate_classify,
            processor_talent_info
        ]

    def process(self, item):
        for processor in self.processors:
            print("running")
            item = processor.process(item)
        return item

    def stats(self):
        stats = {}
        for processor in self.processors:
            stats[processor.name] = processor.stats()
        return stats
