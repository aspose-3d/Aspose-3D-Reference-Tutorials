#!/bin/bash
# Script to verify Java code snippets using javac

TUTORIAL_DIR="/home/lexchou/workspace/aspose/ref-tutorial/3d/english/java"
OUTPUT_DIR="/home/lexchou/workspace/aspose/ref-tutorial/java_verification"
VERSION="26.6.0"
JAR_FILE="/home/lexchou/workspace/aspose/ref-tutorial/aspose-3d-26.6.0.jar"

mkdir -p "$OUTPUT_DIR"

# Initialize counters
total_files=0
java_snippets=0
java_verified=0
java_failed=0

# Create summary file
RESULTS_FILE="$OUTPUT_DIR/results_summary.txt"
echo "Java Code Verification Summary" > "$RESULTS_FILE"
echo "==========================================" >> "$RESULTS_FILE"
echo "Version: $VERSION" >> "$RESULTS_FILE"
echo "" >> "$RESULTS_FILE"

# Track failed snippets
echo "Failed Snippets:" >> "$RESULTS_FILE"
echo "----------------" >> "$RESULTS_FILE"

# Find all _index.md files
mapfile -t md_files < <(find "$TUTORIAL_DIR" -name "_index.md" | sort)

total_files=${#md_files[@]}
echo "Found $total_files tutorial files"

# Process each file
for md_file in "${md_files[@]}"; do
    file_name=$(basename "$(dirname "$md_file")")
    
    echo "Processing: $file_name..."
    
    # Extract Java code blocks between ```java and ```
    while IFS= read -r snippet; do
        # Skip empty snippets
        [ -z "$snippet" ] && continue
        
        java_snippets=$((java_snippets + 1))
        
        # Create temp Java file for verification
        temp_file="/tmp/verify_${file_name}_${java_snippets}.java"
        cat > "$temp_file" << 'JAVAFILE'
import com.aspose.threed.*;
public class TempVerify {
    public static void main(String[] args) {
JAVAFILE
        echo "$snippet" >> "$temp_file"
        echo "    }" >> "$temp_file"
        echo "}" >> "$temp_file"
        
        # Compile with javac
        if javac -cp "$JAR_FILE" "$temp_file" 2>/dev/null; then
            java_verified=$((java_verified + 1))
            echo "  ✓ Snippet $java_snippets verified"
        else
            java_failed=$((java_failed + 1))
            echo "  ✗ Snippet $java_snippets FAILED" >> "$RESULTS_FILE"
            echo "    File: $file_name" >> "$RESULTS_FILE"
            echo "    Code:" >> "$RESULTS_FILE"
            echo "```" >> "$RESULTS_FILE"
            echo "$snippet" >> "$RESULTS_FILE"
            echo "```" >> "$RESULTS_FILE"
            echo "" >> "$RESULTS_FILE"
            
            # Also show error on stderr
            echo "  Error details in $temp_file"
            
            # Try to compile again to see the actual error
            echo "  Compiler output:"
            javac -cp "$JAR_FILE" "$temp_file" 2>&1 | head -10 | sed 's/^/    /'
        fi
        
        rm -f "$temp_file"
        
    done < <(awk '
    BEGIN { in_block = 0; snippet = ""; }
    /^```java/ { in_block = 1; snippet = ""; next; }
    /^```$/ && in_block { 
        if (snippet != "") {
            print snippet
        }
        in_block = 0; snippet = ""; next; 
    }
    in_block { 
        if (snippet != "") snippet = snippet "\n";
        snippet = snippet $0; 
    }
    ' "$md_file")
    
done

# Final summary
echo "" >> "$RESULTS_FILE"
echo "==========================================" >> "$RESULTS_FILE"
echo "FINAL SUMMARY" >> "$RESULTS_FILE"
echo "==========================================" >> "$RESULTS_FILE"
echo "Total files reviewed: $total_files" >> "$RESULTS_FILE"
echo "Java code snippets found: $java_snippets" >> "$RESULTS_FILE"
echo "Java snippets verified successfully: $java_verified" >> "$RESULTS_FILE"
echo "Java snippets with errors: $java_failed" >> "$RESULTS_FILE"

echo ""
echo "========================================="
echo "VERIFICATION COMPLETE"
echo "========================================="
echo "Total files: $total_files"
echo "Java snippets: $java_snippets"
echo "Verified: $java_verified"
echo "Failed: $java_failed"
echo ""
echo "Results saved to: $RESULTS_FILE"
