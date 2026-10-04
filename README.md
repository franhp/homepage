# Homepage

Visit [franhp.dev](https://franhp.dev)

## Installation

### Dependencies

```
brew install spatialite-tools gdal
OR
apt-get install gdal-bin libsqlite3-mod-spatialite
```

```
cd frontend && npm i
```

Install uv for Python dependency management. The backend uses Python 3.14 and Django 6.1.

```
cd backend && uv sync --locked
```

## Running

```
cd backend && uv run --locked python manage.py runserver
```

Or run the admin in Docker:

```
docker compose up --build -d admin
```

Watched titles are synchronized from Floppy (`tracking.franhp.dev`). Configure the
API key without committing it:

```
export FLOPPY_API_KEY=<token>
export FLOPPY_API_URL=https://tracking.franhp.dev # optional
```

On the first migration, match the existing IMDb/Goodreads rows to Floppy and
review the reported unmatched titles:

```
cd backend && uv run --locked python manage.py import_floppy_ids
```

After fixing any missing entries in Floppy, rerun it with `--delete-missing` to
remove titles that are no longer tracked. Then refresh the watched data and
generated JSON:

```
cd backend && uv run --locked python manage.py out_watched --update
```

The same synchronization is available from the Titles admin page.

---

### Ideas

- [ ] top games from grouvee
- [ ] wiki toc

## Pending fixes

- [ ] markdown editor in the admin for wiki
- [ ] Default .env file
- [ ] dockerise checks
- [ ] check links are alive automatically
