#!/bin/bash
# Simple script to extract and verify Java code snippets from tutorial files

TUTORIAL_DIR="/home/lexchou/workspace/aspose/ref-tutorial/3d/english/java"
OUTPUT_DIR="/home/lexchou/workspace/aspose/ref-tutorial/java_verification"
VERSION="26.6.0"

mkdir -p "$OUTPUT_DIR"

# Initialize counters
total_files=0
java_snippets=0
java_verified=0
java_failed=0

# Create temp file for results
RESULTS_FILE="$OUTPUT_DIR/results_summary.txt"
echo "Java Code Verification Summary" > "$RESULTS_FILE"
echo "==========================================" >> "$RESULTS_FILE"
echo "" >> "$RESULTS_FILE"

# Find all _index.md files and process them
echo "Processing tutorial files..."
find "$TUTORIAL_DIR" -name "_index.md" | sort | while read -r md_file; do
    file_name=$(basename $(dirname "$md_file"))
    total_files=$((total_files + 1))
    
    echo "Processing: $file_name ($total_files)"
    
    # Extract Java code blocks
    # Use grep and sed to extract content between java code blocks
    if grep -q '```java' "$md_file" 2>/dev/null; then
        # Extract all java code blocks using awk
        awk '
        BEGIN { in_block = 0; snippet_num = 0; }
        /^```java/ { in_block = 1; snippet_num++; next; }
        /^```/ && in_block { in_block = 0; next; }
        in_block { print; }
        ' "$md_file" | split -l 100 - "$OUTPUT_DIR/${file_name}_snippet_"
        
        # Process each snippet file
        for snippet_file in "$OUTPUT_DIR/${file_name}_snippet_"*; do
            if [ -f "$snippet_file" ]; then
                # Verify the snippet
                echo "Verifying snippet from $file_name..."
                java_snippets=$((java_snippets + 1))
                
                # Create a test Java file
                cat > /tmp/verify_temp.java << 'JAVAFILE'
import com.aspose.threed.*;
public class TempVerify {
    public static void main(String[] args) {
JAVAFILE
                cat "$snippet_file" >> /tmp/verify_temp.java
                echo "    }" >> /tmp/verify_temp.java
                echo "}" >> /tmp/verify_temp.java
                
                # Verify using aspose-cli
                if aspose-cli verify --language java "$VERSION" /tmp/verify_temp.java > /dev/null 2>&1; then
                    java_verified=$((java_verified + 1))
                    echo "  ✓ Verified successfully"
                else
                    java_failed=$((java_failed + 1))
                    echo "  ✗ Verification failed" >> "$RESULTS_FILE"
                    echo "  File: $file_name" >> "$RESULTS_FILE"
                    head -20 "$snippet_file" >> "$RESULTS_FILE"
                    echo "" >> "$RESULTS_FILE"
                    
                    # Show error details
                    aspose-cli verify --language java "$VERSION" /tmp/verify_temp.java 2>&1 | head -50 >> "$RESULTS_FILE"
                    echo "" >> "$RESULTS_FILE"
                    echo "  (Error logged to results)"
                fi
                
                rm -f /tmp/verify_temp.java
            fi
        done
    fi
    
    # Clean up snippet files
    rm -f "$OUTPUT_DIR/${file_name}_snippet_"*
    
    # Report progress every 10 files
    if [ $((total_files % 10)) -eq 0 ]; then
        echo "Progress: $total_files files processed..."
    fi
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
