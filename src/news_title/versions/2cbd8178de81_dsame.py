"""[Dsame

Revision ID: 2cbd8178de81
Revises: dd8659d523b9
Create Date: 2023-02-25 18:29:57.837058

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '2cbd8178de81'
down_revision = 'dd8659d523b9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(table_name='cons_data', column_name='lang')
    op.drop_column(table_name='cons_data', column_name='image_path')


def downgrade() -> None:
    pass
