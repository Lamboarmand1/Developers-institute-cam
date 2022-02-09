"""empty message

Revision ID: bc0dee317016
Revises: 
Create Date: 2021-12-16 16:27:10.349699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc0dee317016'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('classe',
    sa.Column('class_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('is_exam', sa.Boolean(), nullable=True),
    sa.Column('nombre_eleves', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('class_id')
    )
    op.create_table('courses',
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('chapter', sa.Integer(), nullable=True),
    sa.Column('credits', sa.Integer(), nullable=True),
    sa.Column('support', sa.String(length=200), nullable=True),
    sa.Column('_class', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['_class'], ['classe.class_id'], ),
    sa.PrimaryKeyConstraint('course_id')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('inscription_date', sa.DateTime(), nullable=True),
    sa.Column('_class', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['_class'], ['classe.class_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    op.drop_table('courses')
    op.drop_table('classe')
    # ### end Alembic commands ###
