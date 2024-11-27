import uuid
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


# region Rewards
class RewardBase(SQLModel):
    name: str = Field(nullable=False)
    points: int = Field(nullable=False)


class Reward(RewardBase, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, nullable=False)
    activities: List["Activity"] = Relationship(back_populates="reward")


class RewardCreate(RewardBase):
    pass


class RewardRead(RewardBase):
    id: uuid.UUID


class RewardUpdate(RewardBase):
    pass


# endregion


# region Activity
class ActivityBase(SQLModel):
    name: str = Field(nullable=False)
    reward_id: uuid.UUID = Field(foreign_key="reward.id", nullable=False)


class Activity(ActivityBase, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True, nullable=False)
    user_id: Optional[uuid.UUID] = Field(nullable=False)
    reward: Reward = Relationship(back_populates="activities")


class ActivityCreate(ActivityBase):
    pass


class ActivityRead(ActivityBase):
    id: uuid.UUID


class ActivityUpdate(ActivityBase):
    pass


class ActivityReadWithReward(ActivityRead):
    reward: Optional[RewardRead] = None
