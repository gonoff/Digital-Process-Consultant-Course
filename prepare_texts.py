#!/usr/bin/env python3
"""
Text Preparation Script for Haniel Chronicles TTS Conversion
Cleans markdown files and prepares them for speech synthesis.
"""

import os
import re
import shutil
from pathlib import Path

def clean_text_for_tts(content):
    """
    Clean markdown content for text-to-speech optimization.
    Removes navigation, wiki links, and markdown formatting.
    """
    # Remove navigation sections (from ## Navigation to ---)
    content = re.sub(r'## Navigation.*?---\n', '', content, flags=re.DOTALL)
    
    # Remove wiki links but keep display text
    # [[file|display text]] -> display text
    # [[file]] -> file
    content = re.sub(r'\[\[([^|\]]+)\|([^\]]+)\]\]', r'\2', content)
    content = re.sub(r'\[\[([^\]]+)\]\]', r'\1', content)
    
    # Remove markdown headers (# symbols)
    content = re.sub(r'^#{1,6}\s+', '', content, flags=re.MULTILINE)
    
    # Remove markdown emphasis but keep text
    content = re.sub(r'\*\*([^*]+)\*\*', r'\1', content)  # Bold
    content = re.sub(r'\*([^*]+)\*', r'\1', content)      # Italic
    
    # Clean up multiple line breaks
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Remove horizontal rules
    content = re.sub(r'^---+$', '', content, flags=re.MULTILINE)
    
    # Clean up whitespace
    content = content.strip()
    
    return content

def process_story_files():
    """
    Process all story files from /story/ directory to create clean text versions.
    """
    story_dir = Path('story')
    output_dir = Path('story_audio')
    
    if not story_dir.exists():
        print(f"❌ Story directory not found: {story_dir}")
        return
    
    processed_count = 0
    skipped_count = 0
    
    # Define level directories to process
    level_dirs = ['level0', 'level1', 'level2', 'level3', 'level4', 'capstone']
    
    for level_dir in level_dirs:
        level_path = story_dir / level_dir
        output_level_path = output_dir / level_dir / 'text'
        
        if not level_path.exists():
            print(f"⚠️  Level directory not found: {level_path}")
            continue
        
        print(f"\n📂 Processing {level_dir}...")
        
        # Get all .md files in this level
        md_files = list(level_path.glob('*.md'))
        
        for md_file in md_files:
            try:
                # Read the markdown file
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Clean the content for TTS
                cleaned_content = clean_text_for_tts(content)
                
                # Create output filename (change .md to .txt)
                output_filename = md_file.stem + '.txt'
                output_path = output_level_path / output_filename
                
                # Write cleaned content
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(cleaned_content)
                
                # Show character count for reference
                char_count = len(cleaned_content)
                print(f"  ✅ {md_file.name} → {output_filename} ({char_count:,} chars)")
                processed_count += 1
                
            except Exception as e:
                print(f"  ❌ Error processing {md_file.name}: {e}")
                skipped_count += 1
    
    # Process main story index files if they exist
    main_story_files = ['story_index.md', 'story_implementation_plan.md']
    for story_file in main_story_files:
        file_path = story_dir / story_file
        if file_path.exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                cleaned_content = clean_text_for_tts(content)
                output_path = output_dir / (story_file.replace('.md', '.txt'))
                
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(cleaned_content)
                
                char_count = len(cleaned_content)
                print(f"  ✅ {story_file} → {story_file.replace('.md', '.txt')} ({char_count:,} chars)")
                processed_count += 1
                
            except Exception as e:
                print(f"  ❌ Error processing {story_file}: {e}")
                skipped_count += 1
    
    print(f"\n📊 Summary:")
    print(f"  ✅ Processed: {processed_count} files")
    print(f"  ❌ Skipped: {skipped_count} files")
    print(f"  📁 Output directory: {output_dir}")

def create_processing_manifest():
    """
    Create a manifest file listing all text files ready for audio generation.
    """
    output_dir = Path('story_audio')
    manifest_path = output_dir / 'processing_manifest.txt'
    
    text_files = []
    
    # Collect all text files
    for level_dir in ['level0', 'level1', 'level2', 'level3', 'level4', 'capstone']:
        text_dir = output_dir / level_dir / 'text'
        if text_dir.exists():
            for txt_file in text_dir.glob('*.txt'):
                relative_path = txt_file.relative_to(output_dir)
                text_files.append(str(relative_path))
    
    # Add main story files
    for main_file in ['story_index.txt', 'story_implementation_plan.txt']:
        main_path = output_dir / main_file
        if main_path.exists():
            text_files.append(main_file)
    
    # Write manifest
    with open(manifest_path, 'w', encoding='utf-8') as f:
        f.write("# Haniel Chronicles Text Files - Processing Manifest\n")
        f.write(f"# Generated: {len(text_files)} files ready for audio conversion\n\n")
        for file_path in sorted(text_files):
            f.write(f"{file_path}\n")
    
    print(f"\n📋 Processing manifest created: {manifest_path}")
    print(f"   📁 {len(text_files)} text files ready for audio generation")

if __name__ == "__main__":
    print("🎯 Haniel Chronicles Text Preparation")
    print("=====================================")
    
    process_story_files()
    create_processing_manifest()
    
    print("\n✨ Text preparation complete!")
    print("   Next step: Run generate_audio.py to create speech files")