"""rename department

Revision ID: f9c43d5b5383
Revises: 7862347e7d30
Create Date: 2024-07-01 15:05:03.891418

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9c43d5b5383'
down_revision = '7862347e7d30'
branch_labels = None
depends_on = None


def upgrade():
    # Rename 'department' table to 'departments'
    op.rename_table('department', 'departments')


def downgrade():
    # Revert the rename: 'departments' back to 'department'
    op.rename_table('departments', 'department')