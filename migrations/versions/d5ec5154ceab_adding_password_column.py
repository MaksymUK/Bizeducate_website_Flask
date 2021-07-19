"""adding password column

Revision ID: d5ec5154ceab
Revises: 
Create Date: 2021-07-04 07:20:31.361596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5ec5154ceab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('singlecourse',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('paragraph', sa.String(), nullable=False),
    sa.Column('venue', sa.String(), nullable=False),
    sa.Column('dates', sa.DateTime(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('trainer', sa.Text(), nullable=True),
    sa.Column('key_questions', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['dates'], ['courses.date'], ),
    sa.ForeignKeyConstraint(['paragraph'], ['courses.title'], ),
    sa.ForeignKeyConstraint(['venue'], ['courses.country'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('password', sa.String(length=60), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    op.drop_table('singlecourse')
    # ### end Alembic commands ###
