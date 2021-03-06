"""Added required tables

Revision ID: f5ecf7efa541
Revises: 
Create Date: 2021-11-21 10:00:46.545820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5ecf7efa541'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('zoom_event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event', sa.String(length=120), nullable=True),
    sa.Column('payload', sa.JSON(), nullable=True),
    sa.Column('event_ts', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_zoom_event_event'), 'zoom_event', ['event'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_zoom_event_event'), table_name='zoom_event')
    op.drop_table('zoom_event')
    # ### end Alembic commands ###
