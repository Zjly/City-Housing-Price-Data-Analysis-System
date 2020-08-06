"""empty message

Revision ID: 1bd0e84099ff
Revises: a08efe7b534b
Create Date: 2019-12-16 21:12:48.290759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1bd0e84099ff'
down_revision = 'a08efe7b534b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('name',
    sa.Column('num', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('num'),
    sa.UniqueConstraint('num')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('name')
    # ### end Alembic commands ###
