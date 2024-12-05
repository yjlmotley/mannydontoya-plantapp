
<<<<<<< HEAD:migrations/versions/303672c47c35_.py
<<<<<<< HEAD:migrations/versions/303672c47c35_.py
Revision ID: 303672c47c35
Revises: 
Create Date: 2024-11-24 00:11:29.354185
=======
<<<<<<<< HEAD:migrations/versions/ff947bb35ef9_.py
Revision ID: ff947bb35ef9
Revises: 
Create Date: 2024-11-16 00:37:44.247142
========
Revision ID: 24a89a796684
Revises: 
Create Date: 2024-11-16 00:39:17.173589
>>>>>>>> 5b84a9de1b5a97e161a4271a97b64f2d1a789c3a:migrations/versions/24a89a796684_.py
>>>>>>> 0609a6106ec66940fad711faea88981c55055b4a:migrations/versions/24a89a796684_.py

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
<<<<<<< HEAD:migrations/versions/303672c47c35_.py
revision = '303672c47c35'
=======
<<<<<<<< HEAD:migrations/versions/ff947bb35ef9_.py
revision = 'ff947bb35ef9'
========
revision = '24a89a796684'
>>>>>>>> 5b84a9de1b5a97e161a4271a97b64f2d1a789c3a:migrations/versions/24a89a796684_.py
>>>>>>> 0609a6106ec66940fad711faea88981c55055b4a:migrations/versions/24a89a796684_.py
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('username', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('api_plant_id', sa.Integer(), nullable=False),
    sa.Column('common_name', sa.String(length=250), nullable=False),
<<<<<<< HEAD:migrations/versions/303672c47c35_.py
    sa.Column('scientific_name', sa.String(length=250), nullable=True),
    sa.Column('other_name', sa.String(length=250), nullable=True),
    sa.Column('cycle', sa.String(length=250), nullable=True),
    sa.Column('watering', sa.String(length=250), nullable=True),
    sa.Column('sunlight', sa.String(length=250), nullable=True),
    sa.Column('default_image_original_url', sa.String(length=500), nullable=True),
    sa.Column('default_image_medium_url', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
=======
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
>>>>>>> 0609a6106ec66940fad711faea88981c55055b4a:migrations/versions/24a89a796684_.py
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('api_plant_id', sa.Integer(), nullable=False),
    sa.Column('common_name', sa.String(length=250), nullable=False),
    sa.Column('scientific_name', sa.String(length=250), nullable=True),
    sa.Column('other_name', sa.String(length=250), nullable=True),
    sa.Column('cycle', sa.String(length=250), nullable=True),
    sa.Column('watering', sa.String(length=250), nullable=True),
    sa.Column('sunlight', sa.String(length=250), nullable=True),
    sa.Column('default_image_original_url', sa.String(length=500), nullable=True),
    sa.Column('default_image_medium_url', sa.String(length=500), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plants')
    op.drop_table('favorites')
    op.drop_table('users')
    # ### end Alembic commands ###
=======
>>>>>>> 133c63bb9f6a6cb80df5ee5d74df3e6452740326:migrations/versions/24a89a796684_.py
