from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    feature_store_filepath : str
    train_filepath : str
    test_filepath : str


class DataValidationArtifact:...
class DataTransformationArtifact:...
class ModelTrainerArtifact:...
class ModelEvaluationArtifact:...
class ModelPusherArtifact:...