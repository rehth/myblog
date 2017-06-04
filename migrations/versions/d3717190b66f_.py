"""empty message

Revision ID: d3717190b66f
Revises: 3e37eed1b500
Create Date: 2017-06-04 10:23:50.719486

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd3717190b66f'
down_revision = '3e37eed1b500'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('contents', sa.String(length=3000), nullable=True))
    op.drop_column('messages', 'content')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('content', mysql.VARCHAR(length=300), nullable=True))
    op.drop_column('messages', 'contents')
    # ### end Alembic commands ###
