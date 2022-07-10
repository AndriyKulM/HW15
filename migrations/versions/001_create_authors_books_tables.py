"""001_create_authors_books_tables

Revision ID: 001_create_authors_books_tables
Revises: 
Create Date: 2022-07-08 20:33:50.456873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001_create_authors_books_tables'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "authors",
        sa.Column("author_id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(300), nullable=False),
        sa.Column("last_name", sa.String(300), nullable=False)
    )
    op.create_table(
        "books",
        sa.Column("book_id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("title", sa.String(300), nullable=False),
        sa.Column("publisher", sa.String(300), nullable=False),
        sa.Column("description", sa.String(900), nullable=False),
        sa.Column("isbn", sa.Integer, unique=True)
    )



def downgrade() -> None:
    op.drop_table("authors")
    op.drop_table("books")
