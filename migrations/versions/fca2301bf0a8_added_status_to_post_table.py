"""added status to post table

Revision ID: fca2301bf0a8
Revises: 822b8ca31667
Create Date: 2020-11-01 22:31:01.672512

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fca2301bf0a8'
down_revision = '822b8ca31667'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('status', sa.Integer(), nullable=True))
    op.execute("UPDATE post SET  status = 1 WHERE status is NULL")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'status')
    # ### end Alembic commands ###
