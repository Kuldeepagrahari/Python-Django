# 🔁 Quick Comparison Table
# Visibility	Syntax	Outside Access	Use Case
# Public	value	✅ Yes	General-purpose methods/attributes
# Protected	_value	✅ (by convention, don’t)	Internal methods/attributes (subclass use)
# Private	__value	❌ (name mangling)	Sensitive data, internal implementation

# 🔄 In Inheritance
# Member Type	Accessible in Subclass
# Public	✅ Yes
# Protected	✅ Yes (convention)
# Private	❌ No (use name mangling to access)

# ✅ Best Practices
# Use public for APIs intended for public use.

# Use protected when extending in subclasses but don’t want general external access.

# Use private for implementation details you really want to hide.

