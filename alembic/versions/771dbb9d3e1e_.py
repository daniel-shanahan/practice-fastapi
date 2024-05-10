"""empty message

Revision ID: 771dbb9d3e1e
Revises: 0abc96b95c65
Create Date: 2024-05-09 23:07:16.174426

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '771dbb9d3e1e'
down_revision: Union[str, None] = '0abc96b95c65'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
