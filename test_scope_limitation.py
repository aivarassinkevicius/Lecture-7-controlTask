#!/usr/bin/env python3
"""
Test script to verify UAB Sveikata scope limitation functionality
Tests that the app correctly identifies and handles health vs non-health questions
"""

import sys
import os

# Add the current directory to the path so we can import from app.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import is_health_related_question

def test_health_questions():
    """Test questions that should be accepted (health-related)"""
    health_questions = [
        "What exercises are good for back pain?",
        "How often should I exercise?",
        "What's the best diet for weight loss?",
        "Can you recommend cardio exercises?",
        "How do I build muscle strength?",
        "What are symptoms of anxiety?",
        "How much protein should I eat?",
        "What yoga poses help with stress?",
        "How to improve sleep quality?",
        "Best vitamins for energy?"
    ]
    
    print("🏥 Testing HEALTH-related questions (should be ACCEPTED):")
    print("=" * 60)
    
    passed = 0
    total = len(health_questions)
    
    for question in health_questions:
        result = is_health_related_question(question)
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {question}")
        if result:
            passed += 1
    
    print(f"\nHealth questions: {passed}/{total} passed ({passed/total*100:.1f}%)")
    return passed, total

def test_non_health_questions():
    """Test questions that should be refused (non-health-related)"""
    non_health_questions = [
        "What's the weather like today?",
        "How do I fix my computer?",
        "What's the capital of France?",
        "Can you write Python code for me?",
        "What's the latest movie recommendation?",
        "How do I invest in stocks?",
        "What's the best car to buy?",
        "Can you help me with homework?",
        "What's 2+2?",
        "Tell me a joke"
    ]
    
    print("\n🚫 Testing NON-HEALTH questions (should be REFUSED):")
    print("=" * 60)
    
    passed = 0
    total = len(non_health_questions)
    
    for question in non_health_questions:
        result = is_health_related_question(question)
        status = "✅ PASS" if not result else "❌ FAIL"  # We want False for non-health
        print(f"{status} - {question}")
        if not result:  # Success means it was correctly identified as non-health
            passed += 1
    
    print(f"\nNon-health questions: {passed}/{total} passed ({passed/total*100:.1f}%)")
    return passed, total

def test_edge_cases():
    """Test edge cases and ambiguous questions"""
    edge_cases = [
        ("What time is it?", False, "Time question - should be refused"),
        ("How to cook healthy food?", True, "Nutrition-related - should be accepted"),
        ("Best programming language for health apps?", False, "Programming question - should be refused"),
        ("Mental health tips?", True, "Mental health - should be accepted"),
        ("How to manage work stress?", True, "Stress management - should be accepted"),
        ("What's the best phone app?", False, "Technology question - should be refused")
    ]
    
    print("\n⚠️  Testing EDGE CASES:")
    print("=" * 60)
    
    passed = 0
    total = len(edge_cases)
    
    for question, expected, description in edge_cases:
        result = is_health_related_question(question)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"{status} - {question}")
        print(f"     Expected: {expected}, Got: {result} ({description})")
        if result == expected:
            passed += 1
        print()
    
    print(f"Edge cases: {passed}/{total} passed ({passed/total*100:.1f}%)")
    return passed, total

def main():
    """Run all scope limitation tests"""
    print("🧪 UAB SVEIKATA SCOPE LIMITATION TEST")
    print("=" * 60)
    print("Testing the is_health_related_question() function")
    print("This validates Program_description.txt line 28 requirement:")
    print("'The model should only handle its intended task'\n")
    
    # Run all tests
    health_passed, health_total = test_health_questions()
    non_health_passed, non_health_total = test_non_health_questions()
    edge_passed, edge_total = test_edge_cases()
    
    # Calculate overall results
    total_passed = health_passed + non_health_passed + edge_passed
    total_questions = health_total + non_health_total + edge_total
    overall_percentage = (total_passed / total_questions) * 100
    
    print("\n" + "=" * 60)
    print("📊 OVERALL TEST RESULTS:")
    print("=" * 60)
    print(f"Health questions:     {health_passed}/{health_total} passed")
    print(f"Non-health questions: {non_health_passed}/{non_health_total} passed")  
    print(f"Edge cases:           {edge_passed}/{edge_total} passed")
    print(f"TOTAL:                {total_passed}/{total_questions} passed ({overall_percentage:.1f}%)")
    
    if overall_percentage >= 80:
        print("\n🎉 EXCELLENT! Scope limitation is working well!")
        print("✅ UAB Sveikata will properly refuse non-health questions")
    elif overall_percentage >= 60:
        print("\n⚠️  GOOD but needs improvement. Some questions may slip through.")
    else:
        print("\n❌ POOR performance. Scope limitation needs refinement.")
    
    print("\n💡 USAGE EXAMPLES:")
    print("- Health questions will be processed by AI")
    print("- Non-health questions will get polite refusal")
    print("- Edge cases may need manual review")

if __name__ == "__main__":
    main()