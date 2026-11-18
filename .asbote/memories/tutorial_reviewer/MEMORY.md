Based on the daily memory contents, here are the key synthesized lessons and important information:

## Repository State & Workflow

**Latest Reviewed Commit:** `9df472478` (a self-commit for progress tracking)

**All Commits Up to HEAD Have Been Reviewed:** Commits processed include `7be1e2b` (build-node-hierarchies Java tutorial - verified, compiles correctly) and subsequent progress tracking updates.

## Key Workflows Confirmed

**Progress Tracking Workflow:**
- Always read `.claude/progress.md` at session start to find last reviewed commit
- Use `git stash && git pull --rebase && git stash pop` when uncommitted changes block pull
- Process commits in order (oldest first) using `git log --reverse --format='%H' <last-reviewed>..HEAD`
- For each commit, check if tutorial files were modified with: `git show --name-status --format='' <sha> | grep -E '3d/english/(java|net)/.*_index\.md'`
- If no tutorial files changed, it's a self-commit (progress tracking) - update progress and commit
- If tutorial files changed, verify all code snippets against Aspose.3D 26.6.0
- Update `.claude/progress.md` with the commit SHA after review is complete

**Verification Commands:**
- Java code: `aspose-cli verify java 26.6.0 -` (stdin)
- .NET code: `aspose-cli verify csharp 26.6.0 -` (stdin)
- API lookup: `aspose-cli api show` or `aspose-cli api search`

**Code Fixes Verified:**
- `LinearExtrusion` class is the correct class name (not `Extrusion`, `Polygon`, or `Polyline`)
- `Line` and `ArbitraryProfile` classes work correctly with `LinearExtrusion`
- Scene object instantiation and `scene.open()` calls are required for file loading
- Import paths must use correct case (`com.aspose.threed.Scene`, not `com.aspose.threed.scene`)

## Lessons Learned

1. **Self-commits are common:** Many commits only update `.claude/progress.md` - no code verification needed
2. **Always stash first:** When `git pull --rebase` fails, stash → pull → pop is the reliable pattern
3. **Commit by commit:** Never batch multiple commits in progress tracking - each commit records one review step
4. **Push after each commit:** Keep remote synchronized to avoid conflicts
5. **Class name matters:** `LinearExtrusion` is correct, others are invalid in Aspose.3D 26.6.0
6. **Example markers:** Keep `ExStart`/`ExEnd` markers in files but strip them when assembling verification units
