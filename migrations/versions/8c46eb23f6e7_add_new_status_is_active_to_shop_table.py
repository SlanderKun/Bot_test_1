"""add new status 'is_active' to shop table.

Revision ID: 8c46eb23f6e7
Revises: 5ce79ceb5e7b
Create Date: 2023-03-12 14:56:24.268168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c46eb23f6e7'
down_revision = '5ce79ceb5e7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('shops', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('shops', schema=None) as batch_op:
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###