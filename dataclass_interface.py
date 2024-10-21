from dataclasses import dataclass
from typing import Protocol, Generic, Type, TypeVar

class BillingPlanInterface(Protocol):
    num_free_calls: int
    num_free_bytes: int
    glm_call_price: float
    glm_byte_price: float
    user_priority: int

T = TypeVar('T', bound=BillingPlanInterface)

@dataclass
class BillingPlan:
    num_free_calls: int
    num_free_bytes: int
    glm_call_price: float
    glm_byte_price: float
    user_priority: int

# Example usage
billing_plan = BillingPlan(
    num_free_calls=100,
    num_free_bytes=5000,
    glm_call_price=0.02,
    glm_byte_price=0.01,
    user_priority=1
)

class BillingService(Generic[T]):
    def __init__(self, billing_plan_type: Type[T]):
        self.billing_plan_type = billing_plan_type

print(billing_plan)

# Function using TypeVar
def process_billing_plan(plan: T) -> None:
    print(f"Processing plan with {plan.num_free_calls} free calls")

process_billing_plan(billing_plan)

bs = BillingService(BillingPlan)
