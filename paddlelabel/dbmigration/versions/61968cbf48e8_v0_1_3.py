"""v0.2.0

Revision ID: 61968cbf48e8
Revises: 23c1bf9b7f48
Create Date: 2022-10-19 02:03:41.383698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "61968cbf48e8"
down_revision = "23c1bf9b7f48"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("annotation", sa.Column("predicted_by", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("annotation", "predicted_by")
    # ### end Alembic commands ###