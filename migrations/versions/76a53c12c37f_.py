"""empty message

Revision ID: 76a53c12c37f
Revises: c5c0c9bf5921
Create Date: 2017-12-12 18:48:09.505511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76a53c12c37f'
down_revision = 'c5c0c9bf5921'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('calibration_files', sa.Column('csv_file', sa.Text(), nullable=True))
    op.add_column('calibration_files', sa.Column('txt_file', sa.Text(), nullable=True))
    op.drop_column('calibration_files', 'txt_path')
    op.drop_column('calibration_files', 'csv_path')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('calibration_files', sa.Column('csv_path', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('calibration_files', sa.Column('txt_path', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_column('calibration_files', 'txt_file')
    op.drop_column('calibration_files', 'csv_file')
    # ### end Alembic commands ###