"""empty message

Revision ID: dde33be2ab7a
Revises: 8369118943a1
Create Date: 2022-03-06 15:31:29.343260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dde33be2ab7a'
down_revision = '8369118943a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('challenges', sa.Column('category_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'challenges', 'category', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'challenges', type_='foreignkey')
    op.drop_column('challenges', 'category_id')
    # ### end Alembic commands ###
