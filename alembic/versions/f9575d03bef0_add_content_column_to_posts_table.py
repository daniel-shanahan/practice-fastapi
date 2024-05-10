"""add content column to posts table

Revision ID: f9575d03bef0
Revises: f3ef90cb3417
Create Date: 2024-05-09 22:52:07.490701

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f9575d03bef0"
down_revision: Union[str, None] = "f3ef90cb3417"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
