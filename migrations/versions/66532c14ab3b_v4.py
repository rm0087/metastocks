"""v4

Revision ID: 66532c14ab3b
Revises: 72fbab9ce6f2
Create Date: 2024-08-08 21:31:21.553611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66532c14ab3b'
down_revision = '72fbab9ce6f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('company_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('keywords_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_company_table_keywords_id_keyword_table'), 'keyword_table', ['keywords_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('company_table', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_company_table_keywords_id_keyword_table'), type_='foreignkey')
        batch_op.drop_column('keywords_id')

    # ### end Alembic commands ###
