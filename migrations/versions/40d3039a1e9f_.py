"""empty message

Revision ID: 40d3039a1e9f
Revises: bf7add479275
Create Date: 2017-06-02 01:03:55.999531

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '40d3039a1e9f'
down_revision = 'bf7add479275'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('replies', sa.Column('created', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_replies_created'), 'replies', ['created'], unique=False)
    op.drop_index('ix_replies_creat_at', table_name='replies')
    op.drop_column('replies', 'creat_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('replies', sa.Column('creat_at', mysql.DATETIME(), nullable=True))
    op.create_index('ix_replies_creat_at', 'replies', ['creat_at'], unique=False)
    op.drop_index(op.f('ix_replies_created'), table_name='replies')
    op.drop_column('replies', 'created')
    # ### end Alembic commands ###