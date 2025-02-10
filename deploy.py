from azureml.core import Workspace, Model, Environment, Webservice
from azureml.core.model import InferenceConfig
from azureml.core.webservice import AciWebservice

ws = Workspace.from_config()

# Create Environment
env = Environment.from_conda_specification("fastapi-env", "environment.yaml")

# Create Inference Config
inference_config = InferenceConfig(entry_script="score.py", environment=env)

# Define Deployment Config (Using ACI for simplicity)
deployment_config = AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=1)

# Deploy the model
service = Model.deploy(ws, "fastapi-endpoint", [], inference_config, deployment_config)
service.wait_for_deployment(show_output=True)

print("Service URL:", service.scoring_uri)
