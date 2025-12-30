from pathlib import Path


def _load_env_files():
    try:
        from dotenv import load_dotenv
    except Exception:
        return

    here = Path(__file__).resolve()
    # project root is two parents up from this file: /src/mcqgenerator -> /src -> project root
    project_root = here.parents[2]

    candidates = [
        project_root / ".env",
        project_root / "src" / ".env",
        project_root / "src" / "mcqgenerator" / ".env",
        here.parent / ".env",
    ]

    for p in candidates:
        if p.exists():
            load_dotenv(p)
            break


_load_env_files()
