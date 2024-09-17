"""Renaming students to scholars

Revision ID: c1bb9d5c4662
Revises: 791279dd0760
Create Date: 2024-09-17 12:01:00.625040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1bb9d5c4662'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
