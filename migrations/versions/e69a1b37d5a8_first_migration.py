"""first migration

Revision ID: e69a1b37d5a8
Revises:
Create Date: 2021-03-21 19:59:39.654508

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "e69a1b37d5a8"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "movies",
        sa.Column("title", sa.String(length=64), nullable=False),
        sa.Column("release_date", sa.Date(), nullable=False),
        sa.Column(
            "uuid",
            postgresql.UUID(as_uuid=True),
            server_default=sa.text("UUID(gen_random_uuid())"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("uuid", name=op.f("pk_movies")),
        sa.UniqueConstraint("title", name=op.f("uq_movies_title")),
        sa.UniqueConstraint("uuid", name=op.f("uq_movies_uuid")),
    )
    op.create_table(
        "actors",
        sa.Column("movie_uuid", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("name", sa.String(length=64), nullable=False),
        sa.Column("surname", sa.String(length=64), nullable=True),
        sa.Column("age", sa.Integer(), nullable=True),
        sa.Column("gender", sa.String(length=1), nullable=True),
        sa.Column(
            "uuid",
            postgresql.UUID(as_uuid=True),
            server_default=sa.text("UUID(gen_random_uuid())"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["movie_uuid"], ["movies.uuid"], name=op.f("fk_actors_movie_uuid_movies")
        ),
        sa.PrimaryKeyConstraint("uuid", name=op.f("pk_actors")),
        sa.UniqueConstraint("uuid", name=op.f("uq_actors_uuid")),
    )
    op.create_unique_constraint(op.f("uq_actors_uuid"), "actors", ["uuid"])
    op.create_unique_constraint(op.f("uq_movies_uuid"), "movies", ["uuid"])


def downgrade():
    op.drop_constraint(op.f("uq_movies_uuid"), "movies", type_="unique")
    op.drop_constraint(op.f("uq_actors_uuid"), "actors", type_="unique")
    op.drop_table("actors")
    op.drop_table("movies")
