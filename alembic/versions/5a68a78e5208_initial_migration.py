"""initial migration

Revision ID: 5a68a78e5208
Revises: d8a50552aae3
Create Date: 2023-11-09 04:58:21.057004

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5a68a78e5208'
down_revision: Union[str, None] = 'd8a50552aae3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
