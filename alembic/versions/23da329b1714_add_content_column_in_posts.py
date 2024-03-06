"""add Content column in posts

Revision ID: 23da329b1714
Revises: 8e7b4dc126e5
Create Date: 2024-03-05 16:12:27.312880

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '23da329b1714'
down_revision: Union[str, None] = '8e7b4dc126e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String, nullable= False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
