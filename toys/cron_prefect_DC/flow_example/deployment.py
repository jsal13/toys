from prefect.deployments import Deployment
from prefect.server.schemas.schedules import IntervalSchedule
from tutorial_1 import score_a_few_names

deployment_score_a_few_names = Deployment.build_from_flow(
    flow=score_a_few_names,
    name="score-a-few-names",
    parameters={"names": ["Alice", "Beth", "Cudgel", "James", "Dirk"]},
    infra_overrides={"env": {"PREFECT_LOGGING_LEVEL": "DEBUG"}},
    work_pool_name="test-pool",
    schedule=IntervalSchedule(interval=30, timezone="America/Chicago"),
    is_schedule_active=True,
)

if __name__ == "__main__":
    deployment_score_a_few_names.apply()
