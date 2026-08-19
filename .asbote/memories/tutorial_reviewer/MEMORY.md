Based on the recent conversation history, here's the crafted memory:

## Summary of Tutorial Review Workflow

### Current State (as of 2026-08-15)
- **Last reviewed commit**: `07f49b32` (merge of `optimize/3d/java/20260817050925`)
- **Repository state**: Branch `main` at `07f49b32` with recent pull from origin
- **English Java tutorials**: 78 files
- **English .NET tutorials**: 86 files

### Workflow Process
1. **Stash local changes** → **`git pull --rebase`** → **Restore stashed changes**
2. **Check commits since last reviewed** using `git log --reverse --format='%H' <last-reviewed>..HEAD -- 3d/english/java/ 3d/english/net/`
3. **Identify modified tutorials** using `git show --name-status --format='' <sha> | grep -E '3d/english/(java|net)/.*_index\.md'`
4. **Verify code snippets** using `aspose-cli verify java 26.6.0` or `aspose-cli verify csharp 26.6.0`
5. **Fix any errors** using `aspose-cli api show` or `aspose-cli api search` to confirm correct signatures
6. **Propagate fixes to translations** - English is source of truth, translations mirror code blocks
7. **Update progress** in `.claude/progress.md` with the last reviewed commit SHA

### Key Findings
- Commit `07f49b32` modified 5 English tutorials in load-and-save and point-clouds categories
- Recent commits bring in optimization work from `optimize/3d/java/20260817050925` branch
- All verification uses **Aspose.3D 26.6.0** as the version pin
- No new commits with English tutorial changes since `07f49b32`

### Critical Workflow Rules
- Always update `.claude/progress.md` after each commit's review
- Process commits in oldest-first order
- Only review English tutorials - translations mirror the English code blocks
- Use `aspose-cli` for both verification and API lookup
- Never commit/push until the queue is fully processed and progress is up to date
