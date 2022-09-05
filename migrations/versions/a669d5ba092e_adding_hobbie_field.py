"""adding hobbie field

Revision ID: a669d5ba092e
Revises: 
Create Date: 2022-09-05 02:04:03.469046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a669d5ba092e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('personaldata', sa.Column('hobbie', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('personaldata', 'hobbie')
    # ### end Alembic commands ###