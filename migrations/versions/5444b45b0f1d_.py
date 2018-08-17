"""empty message

Revision ID: 5444b45b0f1d
Revises: 
Create Date: 2018-08-17 08:44:51.046742

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5444b45b0f1d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('address', sa.Text(length=50), nullable=False),
    sa.Column('auther', sa.Text(length=50), nullable=False),
    sa.Column('subject', sa.Text(length=300), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    # ### end Alembic commands ###
