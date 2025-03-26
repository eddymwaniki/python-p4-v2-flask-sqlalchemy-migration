"""rename department

Revision ID: bb832e7a4870
Revises: 4be78606b220
Create Date: 2025-03-26 22:03:44.263696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb832e7a4870'
down_revision = '4be78606b220'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
   op.rename_table('departments', 'department')
    # ### end Alembic commands ###
