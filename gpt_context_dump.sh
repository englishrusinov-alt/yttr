find . -type f \
  ! -path "*/.git/*" \
  ! -path "*/.venv/*" \
  ! -path "*/venv/*" \
  ! -path "*/__pycache__/*" \
  ! -path "*/.pytest_cache/*" \
  ! -name "*.pyc" \
  ! -name "*.png" \
  ! -name "*.jpg" \
  ! -name "*.jpeg" \
  ! -name "*.gif" \
  ! -name "*.webp" \
  ! -name "*.pdf" \
  -print0 | sort -z | while IFS= read -r -d '' f; do
    echo "===== BEGIN FILE: $f ====="
    if [ ! -s "$f" ]; then
      echo "[empty file]"
    elif grep -Iq . "$f"; then
      cat "$f"
    else
      echo "[binary or non-text skipped]"
    fi
    echo "===== END FILE: $f ====="
    echo
  done
