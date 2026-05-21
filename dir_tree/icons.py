FILE_ICONS = {
    ".py": "🐍",
    ".js": "📜", ".ts": "📜",
    ".java": "☕",
    ".rs": "🦀",
    ".go": "🐹",
    ".rb": "💎",
    ".html": "🌐",
    ".css": "🎨", ".scss": "🎨",
    ".sh": "🐚", ".bash": "🐚",
    ".md": "🗒️",
    ".txt": "📝",
    ".pdf": "📕",
    ".doc": "📘", ".docx": "📘",
    ".xls": "📗", ".xlsx": "📗",
    ".json": "📋",
    ".yaml": "📐", ".yml": "📐",
    ".toml": "⚙️", ".ini": "⚙️", ".cfg": "⚙️",
    ".csv": "📊",
    ".db": "🗄️", ".sqlite": "🗄️",
    ".png": "🖼️", ".jpg": "🖼️", ".jpeg": "🖼️", ".gif": "🖼️", ".svg": "🖼️",
    ".mp4": "🎬", ".mov": "🎬", ".avi": "🎬",
    ".mp3": "🎵", ".wav": "🎵", ".flac": "🎵",
    ".zip": "📦", ".tar": "📦", ".gz": "📦",
    ".log": "🪵",
    ".pem": "🔒", ".key": "🔒", ".cert": "🔒",
}

SPECIAL_FILE_NAMES = {
    "README.md": "📖",
    "LICENSE": "⚖️",
    "Dockerfile": "🐳",
    "docker-compose.yml": "🐳",
    ".gitignore": "🚫",
    ".dockerignore": "🚫",
    "Makefile": "🔧",
}


def get_file_icon(path):
    if path.name in SPECIAL_FILE_NAMES:
        return SPECIAL_FILE_NAMES[path.name]
    return FILE_ICONS.get(path.suffix.lower(), "📄")
