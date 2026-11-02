import pptx
import sys

sys.stdout.reconfigure(encoding='utf-8')
prs = pptx.Presentation(r'C:\Users\arunk\.gemini\antigravity\brain\87427b1b-8625-473d-acdc-fff8d0537b70\.user_uploaded\media_1793375585008_a52c90a9.pptx')

for idx, s in enumerate(prs.slides):
    print(f"\n==================== SLIDE {idx+1} ====================")
    for s_idx, sh in enumerate(s.shapes):
        if sh.has_text_frame:
            for p_idx, p in enumerate(sh.text_frame.paragraphs):
                txt = p.text.strip()
                if txt:
                    font_sizes = [r.font.size.pt if r.font.size else None for r in p.runs]
                    font_colors = [r.font.color.rgb if r.font.color and hasattr(r.font.color, 'rgb') else None for r in p.runs]
                    bolds = [r.font.bold for r in p.runs]
                    print(f"Shape {s_idx:02d} [{sh.name}] P{p_idx}: '{txt}' (sz={font_sizes}, c={font_colors}, b={bolds})")
        elif sh.shape_type == pptx.enum.shapes.MSO_SHAPE_TYPE.GROUP:
            print(f"Shape {s_idx:02d} [GROUP: {sh.name}]")
            for sub_idx, sub_sh in enumerate(sh.shapes):
                if sub_sh.has_text_frame:
                    for p_idx, p in enumerate(sub_sh.text_frame.paragraphs):
                        txt = p.text.strip()
                        if txt:
                            print(f"    Sub {sub_idx} [{sub_sh.name}] P{p_idx}: '{txt}'")
