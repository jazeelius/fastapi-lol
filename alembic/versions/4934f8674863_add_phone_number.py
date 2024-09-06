"""add phone number

Revision ID: 4934f8674863
Revises: 102db78ec553
Create Date: 2024-09-06 18:29:03.864065

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4934f8674863'
down_revision: Union[str, None] = '102db78ec553'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String, nullable=True))
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    pass
    # ### end Alembic commands ###
