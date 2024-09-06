"""add content column to post table

Revision ID: f465188d97fd
Revises: 3ec5e5f19e7c
Create Date: 2024-09-06 13:42:46.154324

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f465188d97fd'
down_revision: Union[str, None] = '3ec5e5f19e7c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
