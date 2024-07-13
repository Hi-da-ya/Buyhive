"""update user model

Revision ID: cbddd77bc394
Revises: 22471b5a4d0e
Create Date: 2024-07-13 21:01:36.305065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbddd77bc394'
down_revision = '22471b5a4d0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'phone_number')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('phone_number', sa.VARCHAR(length=20), nullable=True))
    # ### end Alembic commands ###
