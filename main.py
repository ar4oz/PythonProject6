
@app.route("/api/scholarship", methods=["POST"])
def scholarship():
    data = request.get_json(silent=True) or request.form

    student_name = (data.get("studentName") or "").strip()
    guardian = (data.get("guardian") or "").strip()
    phone = (data.get("phone") or "").strip()
    email = (data.get("email") or "").strip()
    program = (data.get("program") or "").strip()
    grade = (data.get("grade") or "").strip()
    reason = (data.get("reason") or "").strip()

    missing = [
        field
        for field, value in (
            ("studentName", student_name),
            ("guardian", guardian),
            ("phone", phone),
            ("program", program),
            ("grade", grade),
        )
        if not value
    ]
    if missing:
        return jsonify({"ok": False, "error": "missing_fields", "fields": missing}), 400

    save_to_csv([student_name, guardian, phone, email, program, grade, reason])
    return jsonify({"ok": True, "studentName": student_name})

