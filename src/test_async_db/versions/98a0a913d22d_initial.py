"""initial

Revision ID: 98a0a913d22d
Revises: 
Create Date: 2023-03-09 19:16:42.013331

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '98a0a913d22d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cons_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('entities', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.Column('date', sa.Date(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cons_data_id'), 'cons_data', ['id'], unique=False)
    op.create_table('news_title',
    sa.Column('id', sa.UUID(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('data', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('news_title')
    op.drop_index(op.f('ix_cons_data_id'), table_name='cons_data')
    op.drop_table('cons_data')
    # ### end Alembic commands ###
