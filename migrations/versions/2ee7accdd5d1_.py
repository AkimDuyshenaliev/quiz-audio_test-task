"""empty message

Revision ID: 2ee7accdd5d1
Revises: 
Create Date: 2023-05-18 07:34:30.010900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ee7accdd5d1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('question_text', sa.String(), nullable=True),
    sa.Column('answer_text', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('question_id')
    )
    op.create_index(op.f('ix_question_id'), 'question', ['id'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.UUID(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'token')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=True)
    op.create_table('audioFile',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('fileUUID', sa.UUID(), nullable=False),
    sa.Column('ownerID', sa.Integer(), nullable=False),
    sa.Column('fileLocation', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['ownerID'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', 'fileUUID')
    )
    op.create_index(op.f('ix_audioFile_id'), 'audioFile', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_audioFile_id'), table_name='audioFile')
    op.drop_table('audioFile')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_question_id'), table_name='question')
    op.drop_table('question')
    # ### end Alembic commands ###
